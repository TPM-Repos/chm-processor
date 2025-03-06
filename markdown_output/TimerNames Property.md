       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TimerNames Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [CancelSpecificationTimerTask Class](topic11979.md) : TimerNames Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the name/s of the Timer/s to cancel. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property TimerNames As [FlowProperty(Of String)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CancelSpecificationTimerTask](topic11979.md)
    Dim value As [FlowProperty(Of String)](topic10978.md)
     
    instance.TimerNames = value
     
    value = instance.TimerNames  
  
C#|   
---|---  
      
    
    public [FlowProperty<string>](topic10978.md) TimerNames {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CancelSpecificationTimerTask Class](topic11979.md)   
[CancelSpecificationTimerTask Members](topic11980.md)


