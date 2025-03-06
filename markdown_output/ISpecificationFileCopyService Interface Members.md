![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ISpecificationFileCopyService Interface Members   
See Also Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2316.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : ISpecificationFileCopyService Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ISpecificationFileCopyService](topic2316.md).

# ![](dotnetimages/collapse.gif)Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [CopyDirectory](topic2321.md)| Overloaded. Recursively copies all files in the specified source directory to the target directory using [CopyFile(String,String)](topic2326.md), while maintaining the directory structure, with the ability to overwrite existing files.   
![ Method](dotnetimages/Method.gif)| [CopyFile](topic2325.md)| Overloaded. Copies the given file to the specified target without deleting the source file.   
Top

# ![](dotnetimages/collapse.gif)Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [CopiedFile](topic2329.md)| Raised whenever a file has been copied using [CopyFile(String,String)](topic2326.md) method.   
![ Event](dotnetimages/Event.gif)| [CopyingFile](topic2330.md)| Raised whenever a file is being copied by the [CopyFile(String,String)](topic2326.md) method.   
Top

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationFileCopyService Interface](topic2316.md)   
[DriveWorks Namespace](topic2159.md)


