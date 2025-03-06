![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LoadRangesFromFile Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ExcelDocument Class](topic2834.md) : LoadRangesFromFile Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_overwrite_
    If the ranges from the file should overwrite the existing ones.

Glossary Item Box

Matches range information with ranges from file. Creates missing ranges and removes unused ones. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub LoadRangesFromFile( _
       ByVal _overwrite_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ExcelDocument](topic2834.md)
    Dim overwrite As Boolean
     
    instance.LoadRangesFromFile(overwrite)  
  
C#|   
---|---  
      
    
    public void LoadRangesFromFile( 
       bool _overwrite_
    )  
  
#### Parameters

 _overwrite_
    If the ranges from the file should overwrite the existing ones.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExcelDocument Class](topic2834.md)   
[ExcelDocument Members](topic2835.md)


