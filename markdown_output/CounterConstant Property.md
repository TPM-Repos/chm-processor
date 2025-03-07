Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CounterConstant Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [StartSpecificationTimerTask Class](topic12661.md) : CounterConstant Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the name of the constant where the timer's counter should be stored. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property CounterConstant As [FlowProperty(Of String)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StartSpecificationTimerTask](topic12661.md)
    Dim value As [FlowProperty(Of String)](topic10978.md)
     
    instance.CounterConstant = value
     
    value = instance.CounterConstant  
  
C#|   
---|---  
      
    
    public [FlowProperty<string>](topic10978.md) CounterConstant {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StartSpecificationTimerTask Class](topic12661.md)   
[StartSpecificationTimerTask Members](topic12662.md)


