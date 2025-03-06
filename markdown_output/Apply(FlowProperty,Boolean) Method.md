![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Apply(FlowProperty,Boolean) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic12884.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [FlowPropertyData Class](topic12873.md) > [Apply Method](topic12882.md) : Apply(FlowProperty,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_prop_
    The property to which to apply.

_allowEmptyRule_
    True to allow the rule to be toggled to dynamic even if the rule is empty.

Glossary Item Box

Applies the property data to the given property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Apply( _
       ByVal _prop_ As [FlowProperty](topic10946.md), _
       ByVal _allowEmptyRule_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FlowPropertyData](topic12873.md)
    Dim prop As [FlowProperty](topic10946.md)
    Dim allowEmptyRule As Boolean
     
    instance.Apply(prop, allowEmptyRule)  
  
C#|   
---|---  
      
    
    public void Apply( 
       [FlowProperty](topic10946.md) _prop_ ,
       bool _allowEmptyRule_
    )  
  
#### Parameters

 _prop_
    The property to which to apply.
_allowEmptyRule_
    True to allow the rule to be toggled to dynamic even if the rule is empty.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowPropertyData Class](topic12873.md)   
[FlowPropertyData Members](topic12874.md)   
[Overload List](topic12882.md)

©2024 DriveWorks Ltd. All Rights Reserved.
