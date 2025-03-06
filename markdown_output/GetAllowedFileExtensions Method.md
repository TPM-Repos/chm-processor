![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetAllowedFileExtensions Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [TinyMCEControl Class](topic9204.md) : GetAllowedFileExtensions Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a list of extensions for the files that are allowed to be uploaded with this control. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetAllowedFileExtensions() As HashSet(Of String)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [TinyMCEControl](topic9204.md)
    Dim value As HashSet(Of String)
     
    value = instance.GetAllowedFileExtensions()  
  
C#|   
---|---  
      
    
    public HashSet<string> GetAllowedFileExtensions()  
  
#### Return Value

A collection of extensions parsed from the [UploadFileExtensionFilter](topic9241.md) property.

# ![](dotnetimages/collapse.gif)Remarks

The Hashset is case insensitive.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[TinyMCEControl Class](topic9204.md)   
[TinyMCEControl Members](topic9205.md)


