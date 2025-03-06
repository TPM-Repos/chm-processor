![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FromCondition Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12885.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) : FromCondition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_condition_
    The condition containing the properties to copy.

Glossary Item Box

Gets an array of [FlowPropertyData](topic12873.md) instances for the given condition's properties. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function FromCondition( _
       ByVal _condition_ As [Condition](topic10804.md) _
    ) As [FlowPropertyData()](topic12873.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim condition As [Condition](topic10804.md)
    Dim value() As [FlowPropertyData](topic12873.md)
     
    value = [FlowPropertyData](topic12873.md).FromCondition(condition)  
  
C#|   
---|---  
      
    
    public static [FlowPropertyData[]](topic12873.md) FromCondition( 
       [Condition](topic10804.md) _condition_
    )  
  
#### Parameters

 _condition_
    The condition containing the properties to copy.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)

©2024 DriveWorks Ltd. All Rights Reserved.
