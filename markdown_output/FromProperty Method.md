![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromProperty Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12886.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) : FromProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_prop_
    The flow property containing the data to duplicate.

Glossary Item Box

Gets a [FlowPropertyData](topic12873.md) instance from the given flow property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromProperty( _
       ByVal _prop_ As [FlowProperty](topic10946.md) _
    ) As [FlowPropertyData](topic12873.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim prop As [FlowProperty](topic10946.md)
    Dim value As [FlowPropertyData](topic12873.md)
     
    value = [FlowPropertyData](topic12873.md).FromProperty(prop)  
  
C#|   
---|---  
      
    
    public static [FlowPropertyData](topic12873.md) FromProperty( 
       [FlowProperty](topic10946.md) _prop_
    )  
  
#### Parameters

 _prop_
    The flow property containing the data to duplicate.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)

©2024 DriveWorks Ltd. All Rights Reserved.
