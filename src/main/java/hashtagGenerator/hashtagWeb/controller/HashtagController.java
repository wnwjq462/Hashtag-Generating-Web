package hashtagGenerator.hashtagWeb.controller;

import hashtagGenerator.hashtagWeb.SocketClient;
import hashtagGenerator.hashtagWeb.service.HashtagService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;

import javax.validation.Valid;

@Controller
@RequiredArgsConstructor
public class HashtagController {

    private final HashtagService hashtagService;

    @GetMapping("/")
    public String hashtag(Model model) {
        return "index";
    }


    @PostMapping("/")
    public String postImage(@RequestParam("photo")MultipartFile file, Model model) throws Exception {
        String savedFileName = hashtagService.fileHandler(file);
        System.out.println(savedFileName);
        String hasgtags = SocketClient.connect(savedFileName);
        model.addAttribute("data", hasgtags);
        return "index";
    }
}
