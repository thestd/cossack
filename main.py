from src.manager import run

if __name__ == '__main__':
    run()

#
# # ========== LOGGING ==========
# if settings.LOGGING_ENABLE:
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
#     logger = logging.getLogger(__name__)
#
#     def error(bot, update, error):
#         logger.warning('Update "%s" caused error "%s"', update, error)
#
#     dispatcher.add_error_handler(error)
