import dataclasses


@dataclasses.dataclass
class Channel:
    no: int
    channel_name: str
    receive_frequency: str
    transmit_frequency: str
    channel_type: str
    transmit_power: str
    band_width: float
    ctss_dcs_decode: float
    ctss_dcs_encode: float
    contact: str
    contact_call_type: str
    contact_tg_dmr_id: str
    radio_id: str
    busy_lock_tx_permit: str
    squelch_mode: str
    optional_signal: float
    dtmf_id: ???
    two_tone_id: ???
    five_tone_id: ???
    ptt_id: ???
    colour_code: int
    slot: int
    scan_list: ???
    receive_group: ???
    receive_group_list: ???
    ptt_prohibit:
    reverse: ???
    simplex_tdma: ???
    slot_suit:
    aes_digital_encryption:
    digital_encryption:
    call_confirmation:
    talk_around_simplex:
    work_alone
    custom_ctcss
    two_tone_decode
    ranging:
    throug_mode:
    digi_aprs_rx
    analog_aprs_ptt_mode
    digital_aprs_ptt_mode
    aprs_report_type
    digital_aprs_report_channel
    correct_frequency_hz
    sms_confirmation
    exclude_channel_from_roaming
    dmr_mode
    dataack_disable
    r5tone_bot
    r5tone_eot



"No.","Channel Name","Receive Frequency","Transmit Frequency","Channel Type","Transmit Power","Band Width","CTCSS/DCS Decode","CTCSS/DCS Encode","Contact","Contact Call Type","Contact TG/DMR ID","Radio ID","Busy Lock/TX Permit","Squelch Mode","Optional Signal","DTMF ID","2Tone ID","5Tone ID","PTT ID","Color Code","Slot","Scan List","Receive Group List","PTT Prohibit","Reverse","Simplex TDMA","Slot Suit","AES Digital Encryption","Digital Encryption","Call Confirmation","Talk Around(Simplex)","Work Alone","Custom CTCSS","2TONE Decode","Ranging","Through Mode","Digi APRS RX","Analog APRS PTT Mode","Digital APRS PTT Mode","APRS Report Type","Digital APRS Report Channel","Correct Frequency[Hz]","SMS Confirmation","Exclude channel from roaming","DMR MODE","DataACK Disable","R5toneBot","R5ToneEot"
