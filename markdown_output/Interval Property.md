Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Interval Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [StartSpecificationTimerTask Class](topic12661.md) : Interval Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the interval of how often the timer should run. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Interval As [FlowProperty(Of Double)](topic10978.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StartSpecificationTimerTask](topic12661.md)
    Dim value As [FlowProperty(Of Double)](topic10978.md)
     
    instance.Interval = value
     
    value = instance.Interval  
  
C#|   
---|---  
      
    
    public [FlowProperty<double>](topic10978.md) Interval {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[StartSpecificationTimerTask Class](topic12661.md)   
[StartSpecificationTimerTask Members](topic12662.md)


