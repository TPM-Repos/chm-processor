![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyFile(String,String,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2327.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ISpecificationFileCopyService Interface](topic2316.md) > [CopyFile Method](topic2325.md) : CopyFile(String,String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_source_
    The path to the file to copy.

_target_
    The path to copy the file to.

_deleteSource_
    Whether to delete the source file after the file has been copied.

Glossary Item Box

Copies the given file to the specified target and optionally deletes the source file. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub CopyFile( _
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
     
    instance.CopyFile(source, target, deleteSource)  
  
C#|   
---|---  
      
    
    void CopyFile( 
       string _source_ ,
       string _target_ ,
       bool _deleteSource_
    )  
  
#### Parameters

 _source_
    The path to the file to copy.
_target_
    The path to copy the file to.
_deleteSource_
    Whether to delete the source file after the file has been copied.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationFileCopyService Interface](topic2316.md)   
[ISpecificationFileCopyService Members](topic2317.md)   
[Overload List](topic2325.md)

©2024 DriveWorks Ltd. All Rights Reserved.
