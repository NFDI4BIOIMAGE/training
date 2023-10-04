# YML format

In this repository, we store training materials using a simple YML format. These files are structured like this:

```
- resources
  - name: NFDI4BioImageWebsite
    url: https://nfdi4bioimage.de 
```

These entries can have multiple properties:

* `name` (mandatory): A descriptive title of the resource
* `url` (mandatory): Resources must be available on the internet using a URL or DOI-URL.
* `type` (mandatory): Content types such as `video`, `collection`, `blog post` etc. Resources can have multiple content types.
* `description` (optional)
* `publication_date` (optional)
* `authors` (optional)
* `tags` (optional)

This list of meta-data entries is extensible, just let us know using a [github-issue](https://github.com/haesleinhuepf/training/issues) which kind of meta data you would like to add here.