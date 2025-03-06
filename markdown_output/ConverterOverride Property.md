![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConverterOverride Property   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9464.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [DynamicPropertyData Class](topic9456.md) : ConverterOverride Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/Sets an overridden mechanism for converting values to and from their native representation in the backing store. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property ConverterOverride As [IPropertyValueConverter](topic9373.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [DynamicPropertyData](topic9456.md)
    Dim value As [IPropertyValueConverter](topic9373.md)
     
    instance.ConverterOverride = value
     
    value = instance.ConverterOverride  
  
C#|   
---|---  
      
    
    public [IPropertyValueConverter](topic9373.md) ConverterOverride {get; set;}  
  
# ![](dotnetimages/collapse.gif)Remarks

This can for instance be used to add null handling to a type which would not typically support it.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[DynamicPropertyData Class](topic9456.md)   
[DynamicPropertyData Members](topic9457.md)

©2024 DriveWorks Ltd. All Rights Reserved.
