![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RangeExists Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2850.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ExcelDocument Class](topic2834.md) : RangeExists Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_rangeName_
    Name of the range to find the existence of.

Glossary Item Box

Sees if a given range exists with a specific name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function RangeExists( _
       ByVal _rangeName_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ExcelDocument](topic2834.md)
    Dim rangeName As String
    Dim value As Boolean
     
    value = instance.RangeExists(rangeName)  
  
C#|   
---|---  
      
    
    public bool RangeExists( 
       string _rangeName_
    )  
  
#### Parameters

 _rangeName_
    Name of the range to find the existence of.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ExcelDocument Class](topic2834.md)   
[ExcelDocument Members](topic2835.md)

©2024 DriveWorks Ltd. All Rights Reserved.
