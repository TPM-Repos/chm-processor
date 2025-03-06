![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskReleaseCondition Class   
[Members](topic6648.md) Example   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) : ComponentTaskReleaseCondition Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents a condition which governs whether a [ComponentTask](topic6407.md) getes released during the release process. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image348.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class ComponentTaskReleaseCondition 
       Inherits DriveWorks.DomainObject
       Implements [DriveWorks.Extensibility.IExtension](topic7152.md)   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseCondition](topic6647.md)  
  
C#|   
---|---  
      
    
    public abstract class ComponentTaskReleaseCondition : DriveWorks.DomainObject, [DriveWorks.Extensibility.IExtension](topic7152.md)    
  
# ![](dotnetimages/collapse.gif)Example

Visual Basic| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    <ComponentTaskCondition("Check Value", 
                            "Passes the condition if the rule written for the Condition Result property results in the value TRUE.", 
                            "embedded://MyTasksAndConditions.Puzzle-16x16.png", 
                            "Logic")>
    Public Class CheckValueCondition
        Inherits ComponentTaskReleaseCondition
    
        Private myProperty As FlowProperty(Of Boolean) = Me.Properties.RegisterBooleanProperty("Condition Result", "TRUE to pass the condition")
     
        Protected Overrides Function Evaluate(ByVal specificationContext As SpecificationContext) As Boolean 
            Return myProperty.Value
        End Function
    End Class  
  
# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
**DriveWorks.Components.Tasks.ComponentTaskReleaseCondition**  
[DriveWorks.Components.Tasks.StandardConditions.CheckValueComponentTaskReleaseCondition](topic6737.md)  
[DriveWorks.Components.Tasks.StandardConditions.ReleaseToAutopilotCondition](topic6746.md)  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskReleaseCondition Members](topic6648.md)   
[DriveWorks.Components.Tasks Namespace](topic6391.md)


