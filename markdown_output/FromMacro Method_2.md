![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromMacro Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13146.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [StartNodeRef Class](topic13140.md) : FromMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_macro_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromMacro( _
       ByVal _macro_ As [SpecificationMacro](topic11429.md) _
    ) As [StartNodeRef](topic13140.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim macro As [SpecificationMacro](topic11429.md)
    Dim value As [StartNodeRef](topic13140.md)
     
    value = [StartNodeRef](topic13140.md).FromMacro(macro)  
  
C#|   
---|---  
      
    
    public static [StartNodeRef](topic13140.md) FromMacro( 
       [SpecificationMacro](topic11429.md) _macro_
    )  
  
#### Parameters

 _macro_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StartNodeRef Class](topic13140.md)   
[StartNodeRef Members](topic13141.md)

©2024 DriveWorks Ltd. All Rights Reserved.
