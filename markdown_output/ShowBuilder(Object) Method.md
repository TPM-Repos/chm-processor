![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ShowBuilder(Object) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1605.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Administrator.Extensibility.RulesBuilder Namespace](topic1581.md) > [IRulesBuilderService Interface](topic1598.md) > [ShowBuilder Method](topic1604.md) : ShowBuilder(Object) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The rules aware object, for example, a [DriveWorks.ProjectVariable](topic4927.md), an object implementing [DriveWorks.Abstractions.IHasRule](topic5947.md), or an array of such objects.

Glossary Item Box

Shows the rules builder for the given rules-aware object. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function ShowBuilder( _
       ByVal _context_ As Object _
    ) As [RulesBuilderResult](topic1622.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IRulesBuilderService](topic1598.md)
    Dim context As Object
    Dim value As [RulesBuilderResult](topic1622.md)
     
    value = instance.ShowBuilder(context)  
  
C#|   
---|---  
      
    
    [RulesBuilderResult](topic1622.md) ShowBuilder( 
       object _context_
    )  
  
#### Parameters

 _context_
    The rules aware object, for example, a [DriveWorks.ProjectVariable](topic4927.md), an object implementing [DriveWorks.Abstractions.IHasRule](topic5947.md), or an array of such objects.

#### Return Value

A result object.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IRulesBuilderService Interface](topic1598.md)   
[IRulesBuilderService Members](topic1599.md)   
[Overload List](topic1604.md)

©2024 DriveWorks Ltd. All Rights Reserved.
