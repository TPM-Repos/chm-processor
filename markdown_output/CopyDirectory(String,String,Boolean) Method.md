![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyDirectory(String,String,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2323.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISpecificationFileCopyService Interface](topic2316.md) > [CopyDirectory Method](topic2321.md) : CopyDirectory(String,String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_source_
    The directory to copy files from.

_target_
    The directory to copy files to.

_deleteSource_
    True if the source folder should be deleted after all files have been copied.

Glossary Item Box

Recursively copies all files in the specified source directory to the target directory using [CopyFile(String,String)](topic2326.md), while maintaining the directory structure. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub CopyDirectory( _
       ByVal _source_ As String, _
       ByVal _target_ As String, _
       ByVal _deleteSource_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFileCopyService](topic2316.md)
    Dim source As String
    Dim target As String
    Dim deleteSource As Boolean
     
    instance.CopyDirectory(source, target, deleteSource)  
  
C#|   
---|---  
      
    
    void CopyDirectory( 
       string _source_ ,
       string _target_ ,
       bool _deleteSource_
    )  
  
#### Parameters

 _source_
    The directory to copy files from.
_target_
    The directory to copy files to.
_deleteSource_
    True if the source folder should be deleted after all files have been copied.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationFileCopyService Interface](topic2316.md)   
[ISpecificationFileCopyService Members](topic2317.md)   
[Overload List](topic2321.md)

©2024 DriveWorks Ltd. All Rights Reserved.
