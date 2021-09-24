import functools
import inspect
import logging
from datetime import datetime
from pathlib import Path


def log(func):
    # Declared for use by the whole function but reset by wrapper function due to an issue with freeze_time in
    # testing classes
    start_time = datetime.now()

    def pre_function_log(function, args, kwargs, is_async):
        logger = get_logger(function)
        if logger.isEnabledFor(logging.DEBUG) or logger.isEnabledFor(logging.INFO):
            logger.info(f"----------pre function call log----------")
            logger.info(f"Module name:            {function.__module__}")
            logger.info(f"Method name:            {function.__qualname__}")
            if is_async:
                logger.debug(f'Method type:            asynchronous')
            else:
                logger.debug(f'Method type:           synchronous')
            logger.debug(f"Working directory:     {Path.cwd()}")
            logger.debug(f"Start time:            {start_time}")
            logger.info(
                f"Variables:              {pre_function_info_signature(function=function, args=args, kwargs=kwargs)}"
            )

    def post_function_log(function, result):
        logger = get_logger(function)
        if logger.isEnabledFor(logging.DEBUG) or logger.isEnabledFor(logging.INFO):
            logger.info(f"----------post function call log----------")
            logger.info(f"Module name:            {function.__module__}")
            logger.info(f"Method name:            {function.__qualname__}")

            finish_time = datetime.now()
            logger.debug(f"End time:              {finish_time}")
            difference = finish_time - start_time
            elapsed_time = difference.total_seconds()
            logger.info(f"Elapsed time:           {elapsed_time}")
            logger.info(
                f"Returns:                {post_function_info_signature(result=result)}"
            )

            logger.info(
                f"_______________________________________________________________________________________"
            )

    def pre_function_info_signature(function, args, kwargs):
        bound_args = inspect.signature(function).bind(*args, **kwargs)
        bound_args.apply_defaults()
        loop_count = 0
        args_display = []
        for a in bound_args.arguments.items():
            if a[0] != "self":
                arg_display = f"{a[0]}: {type(a[1]).__name__} = {a[1]}"
                args_display.append(arg_display)
            loop_count += 1

        # TODO check display is correct for kwargs
        kwargs_display = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_display + kwargs_display)
        return signature

    def post_function_info_signature(result):
        if type(result) is tuple:
            signature = post_function_tuple_signature(result)

        else:
            signature = f"{type(result).__name__} = {result}"

        return signature

    def post_function_tuple_signature(result):
        signature = f"tuple["
        count = 0
        for r in result:
            if count > 0:
                signature += f", "
            signature += f"{type(r).__name__} = {r}"
            count += 1
        signature += f"]"
        return signature

    def function_error_log(function, exception):
        logger = get_logger(function=function)
        logger.exception(f"-----------------error log-----------------")
        logger.exception(exception)
        result = None
        return result

    def get_logger(function):
        logger_name = function.__module__
        logger = logging.getLogger(logger_name)
        return logger

    if inspect.iscoroutinefunction(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal start_time
            start_time = datetime.now()
            async_result = None
            try:
                pre_function_log(func, args, kwargs, True)
                async_result = await func(*args, **kwargs)
            except Exception as e:  # only called if exception not caught is code or re-raised by function
                function_error_log(function=func, exception=e)
                raise
            finally:
                post_function_log(func, async_result)
            return async_result

        return wrapper
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal start_time
            start_time = datetime.now()
            result = None
            try:
                pre_function_log(func, args, kwargs, False)
                result = func(*args, **kwargs)

            except Exception as e:  # only called if exception not caught is code or re-raised by function
                function_error_log(function=func, exception=e)
                raise
            finally:
                post_function_log(func, result)
            return result

        return wrapper
