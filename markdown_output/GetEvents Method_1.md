Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEvents Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IApplicationEventService Interface](topic49.md) : GetEvents Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the events in the event log. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetEvents() As [IApplicationEvent()](topic36.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IApplicationEventService](topic49.md)
    Dim value() As [IApplicationEvent](topic36.md)
     
    value = instance.GetEvents()  
  
C#|   
---|---  
      
    
    [IApplicationEvent[]](topic36.md) GetEvents()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IApplicationEventService Interface](topic49.md)   
[IApplicationEventService Members](topic50.md)


