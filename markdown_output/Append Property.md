Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Append Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [SetStatesToTriggerOnTask Class](topic12600.md) : Append Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets whether to append the new states to trigger on. False if we want to replace the existing states. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Append As [FlowProperty(Of Boolean)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SetStatesToTriggerOnTask](topic12600.md)
    Dim value As [FlowProperty(Of Boolean)](topic10978.md)
     
    instance.Append = value
     
    value = instance.Append  
  
C#|   
---|---  
      
    
    public [FlowProperty<bool>](topic10978.md) Append {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SetStatesToTriggerOnTask Class](topic12600.md)   
[SetStatesToTriggerOnTask Members](topic12601.md)


