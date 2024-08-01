<script setup>
import MarkdownIt from "markdown-it";
import MarkdownItAbbr from "markdown-it";
import MarkdownItAnchor from "markdown-it";
import MarkdownItFootnote from "markdown-it";
import MarkdownItHighlightjs from "markdown-it";
import MarkdownItSub from "markdown-it";
import MarkdownItSup from "markdown-it";
import MarkdownItTasklists from "markdown-it";

const markdown = new MarkdownIt()
markdown.use(MarkdownItAbbr)
markdown.use(MarkdownItAnchor)
markdown.use(MarkdownItFootnote)
markdown.use(MarkdownItHighlightjs)
markdown.use(MarkdownItSub)
markdown.use(MarkdownItSup)
markdown.use(MarkdownItTasklists);

defineProps({
    question: String,
    answer: String,
})

</script>

<template>
    <div>
        <h3 class="q-show left-align">{{ question }}</h3>
        <!-- <p class="answer left-align">{{ answer }}</p> -->
        <div class="a-show left-align" v-html="markdown.render(answer)" />
    </div>
</template>

<style scoped>
.q-show {
    width: 1000px;
}

.a-show {
    width: 1000px;
    border: 1px solid green;
    border-radius: 8px;
    /* 设置圆角大小 */
}

.left-align {
    text-align: left;
    padding: 10px;
}
</style>
