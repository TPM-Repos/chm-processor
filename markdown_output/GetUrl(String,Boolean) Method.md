![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetUrl(String,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6000.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IResourceUrlProvider Interface](topic5993.md) > [GetUrl Method](topic5998.md) : GetUrl(String,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_resourcePath_
    The full path to the file.

_allowFilePaths_
    Whether or not the path can be returned to us if we're in an environment that wants that (i.e. desktop).

Glossary Item Box

Gets the URL for the specified file. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function GetUrl( _
       ByVal _resourcePath_ As String, _
       ByVal _allowFilePaths_ As Boolean _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IResourceUrlProvider](topic5993.md)
    Dim resourcePath As String
    Dim allowFilePaths As Boolean
    Dim value As String
     
    value = instance.GetUrl(resourcePath, allowFilePaths)  
  
C#|   
---|---  
      
    
    string GetUrl( 
       string _resourcePath_ ,
       bool _allowFilePaths_
    )  
  
#### Parameters

 _resourcePath_
    The full path to the file.
_allowFilePaths_
    Whether or not the path can be returned to us if we're in an environment that wants that (i.e. desktop).

#### Return Value

The URL to the specified file or the original file path.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IResourceUrlProvider Interface](topic5993.md)   
[IResourceUrlProvider Members](topic5994.md)   
[Overload List](topic5998.md)

©2024 DriveWorks Ltd. All Rights Reserved.
