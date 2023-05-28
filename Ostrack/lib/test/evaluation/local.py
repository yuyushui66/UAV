from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/got10k_lmdb'
    settings.got10k_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/itb'
    settings.lasot_extension_subset_path_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/lasot_lmdb'
    settings.lasot_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/lasot'
    settings.network_path = '/root/autodl-tmp/ostrack/OSTrack-main/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/nfs'
    settings.otb_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/otb'
    settings.prj_dir = '/root/autodl-tmp/ostrack/OSTrack-main'
    settings.result_plot_path = '/root/autodl-tmp/ostrack/OSTrack-main/output/test/result_plots'
    settings.results_path = '/root/autodl-tmp/ostrack/OSTrack-main/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/root/autodl-tmp/ostrack/OSTrack-main/output'
    settings.segmentation_path = '/root/autodl-tmp/ostrack/OSTrack-main/output/test/segmentation_results'
    settings.tc128_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/trackingnet'
    settings.uav_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/uav'
    settings.vot18_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/vot2018'
    settings.vot22_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/vot2022'
    settings.vot_path = '/root/autodl-tmp/ostrack/OSTrack-main/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

