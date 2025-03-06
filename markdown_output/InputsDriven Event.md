![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InputsDriven Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationRequest Interface](topic1778.md) : InputsDriven Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the inputs are driven into to the specification. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event InputsDriven As EventHandler(Of SpecificationRequestInputsDrivenEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequest](topic1778.md)
    Dim handler As EventHandler(Of SpecificationRequestInputsDrivenEventArgs)
     
    AddHandler instance.InputsDriven, handler  
  
C#|   
---|---  
      
    
    event EventHandler<SpecificationRequestInputsDrivenEventArgs> InputsDriven  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [SpecificationRequestInputsDrivenEventArgs](topic1960.md) containing data related to this event. The following **SpecificationRequestInputsDrivenEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
Cancel|  (Inherited from System.ComponentModel.CancelEventArgs)  
[FailedInputNames](topic1967.md)| Gets the names of the inputs that were unable to be driven.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[ISpecificationRequest Members](topic1779.md)


