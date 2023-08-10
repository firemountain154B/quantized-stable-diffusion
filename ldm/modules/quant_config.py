from typing import Dict

def add_int_recursive(item, add_value):
    if isinstance(item, int):
        return item + add_value
    elif isinstance(item, list):
        return [add_int_recursive(element, add_value) for element in item]
    elif isinstance(item, dict):
        return {key: add_int_recursive(value, add_value) if not isinstance(value, bool) else value for key, value in item.items()}
    else:
        return item

class CelebA256UNetQuantConfig():
    def __init__(self, bitwidth=8) -> None:
        self.quant_config = {}
        self.config_keys = [
            "attpool_qkf", 
            "attpool_c",
            "upsample",
            "downsample",
            "avg_pool2d",
            "silu_res_in",
            "resblock_in",
            "silu_res_emb",
            "resblock_emb",
            "silu_res_out",
            "resblock_out",
            "resblock_skip",
            "attblock_qkv",
            "attblock_out",
            "temb_1",
            "silu_temb",
            "temb_2",
            "unet_in",
            "silu_unet_out",
            "unet_out",
            "unet_codebook",
            ]
        
        self.quant_config["attpool_qkf"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["attpool_c"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["unet_codebook"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["avg_pool2d"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        
        """
        self.quant_config["upsample"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["downsample"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["avg_pool2d"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["silu_res_in"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["resblock_in"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["silu_res_emb"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["resblock_emb"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["silu_res_out"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["resblock_out"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["resblock_skip"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["attblock_qkv"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["attblock_out"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["unet_temb"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["silu_unet_temb"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["unet_in"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}
        self.quant_config["silu_unet_out"] = {"bypass": True, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 5}
        self.quant_config["unet_out"] = {"bypass": True, "name": "integer", "weight_width": 8, "weight_frac_width": 5,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 5}

        """


        self.quant_config["temb_1"] = {"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 7, 
                                            "bias_width": 8, "bias_frac_width": 11}
        self.quant_config["silu_temb"] = {"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 4}
        self.quant_config["temb_2"] = {"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9}
        self.quant_config["unet_in"] = {"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9}
        # Begin ResBlock[0]
        self.quant_config["silu_res_in"] = [{"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 4}]
        self.quant_config["resblock_in"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9}]
        self.quant_config["silu_res_emb"] = [{"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2}]
        self.quant_config["resblock_emb"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9}]
        self.quant_config["silu_res_out"] = [{"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2}]
        self.quant_config["resblock_out"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10}]
        self.quant_config["resblock_skip"] = [None]

        # Begin Resblock[1]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 4})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append(None)

        # Begin DownSample[0]
        self.quant_config["downsample"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10}]
        
        # Begin ResBlock[2]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[0]
        self.quant_config["attblock_qkv"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 7}]
        self.quant_config["attblock_out"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9}]
        
        # Begin ResBlock[3]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append(None)

        # Begin AttentionBlock[1]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 7})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        
        # Begin DownSample[1]
        self.quant_config["downsample"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin ResBlock[4]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 10,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[2]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[5]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append(None)
        
        # Begin AttentionBlock[3]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin DownSample[2]
        self.quant_config["downsample"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin ResBlock[6]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 4})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 10,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[4]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin ResBlock[7]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 11})
        self.quant_config["resblock_skip"].append(None)
        
        # Begin AttentionBlock[5]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 11})
        
        # Begin MiddleBlock
        # Begin ResBlock[8]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append(None)

        # Begin AttentionBlock[6]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[9]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append(None)

        # Begin OutBlock
        # Begin ResBlock[10]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin AttentionBlock[7]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[11]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 1})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 1, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 0, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin AttentionBlock[8]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[12]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 7})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 7})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin AttentionBlock[8]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin Upsample[0]
        self.quant_config["upsample"] = [{"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 8}]
        
        # Begin ResBlock[13]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 1, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[9]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[14]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 10,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[10]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})

        # Begin ResBlock[15]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 10,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin AttentionBlock[11]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin Upsample[1]
        self.quant_config["upsample"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        
        # Begin ResBlock[16]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 1, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[12]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[17]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin AttentionBlock[13]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[18]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin AttentionBlock[14]
        self.quant_config["attblock_qkv"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 8})
        self.quant_config["attblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin Upsample[2]
        self.quant_config["upsample"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 8})
        
        # Begin ResBlock[19]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 0, 
                                            "bias_width": 8, "bias_frac_width": 9})
        
        # Begin ResBlock[20]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 1, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin ResBlock[21]
        self.quant_config["silu_res_in"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_in"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 3,
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_emb"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 2})
        self.quant_config["resblock_emb"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 7,
                                            "data_in_width": 8, "data_in_frac_width": 3, 
                                            "bias_width": 8, "bias_frac_width": 9})
        self.quant_config["silu_res_out"].append({"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 3})
        self.quant_config["resblock_out"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 6,
                                            "data_in_width": 8, "data_in_frac_width": 4, 
                                            "bias_width": 8, "bias_frac_width": 10})
        self.quant_config["resblock_skip"].append({"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 8,
                                            "data_in_width": 8, "data_in_frac_width": 2, 
                                            "bias_width": 8, "bias_frac_width": 10})
        
        # Begin unet.out
        self.quant_config["silu_unet_out"] = {"bypass": False, "name": "integer",
                                           "data_in_width": 8, "data_in_frac_width": 4}
        self.quant_config["unet_out"] = {"bypass": False, "name": "integer", "weight_width": 8, "weight_frac_width": 9,
                                            "data_in_width": 8, "data_in_frac_width": 5, 
                                            "bias_width": 8, "bias_frac_width": 13}
        
        self.quant_config = add_int_recursive(self.quant_config, bitwidth - 8)
        print(self.quant_config)

        print("Loaded quantization config.")
    
    def get(self, item: str) -> Dict:
        if item in self.config_keys:
            return self.quant_config[item]
        else:
            return None