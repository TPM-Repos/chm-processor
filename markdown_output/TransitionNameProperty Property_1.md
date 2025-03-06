       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TransitionNameProperty Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [InvokeChildSpecificationTransitionTask Class](topic12330.md) : TransitionNameProperty Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the flow property responsible for the name of the transition to invoke on the child specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property TransitionNameProperty As [FlowProperty(Of String)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [InvokeChildSpecificationTransitionTask](topic12330.md)
    Dim value As [FlowProperty(Of String)](topic10978.md)
     
    value = instance.TransitionNameProperty  
  
C#|   
---|---  
      
    
    public [FlowProperty<string>](topic10978.md) TransitionNameProperty {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[InvokeChildSpecificationTransitionTask Class](topic12330.md)   
[InvokeChildSpecificationTransitionTask Members](topic12331.md)


