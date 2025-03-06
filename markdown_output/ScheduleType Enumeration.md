       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ScheduleType Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Connectors.Schedule Namespace](topic6848.md) : ScheduleType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The type of schedule to use for the connector. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ScheduleType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ScheduleType](topic6850.md)  
  
C#|   
---|---  
      
    
    public enum ScheduleType : System.Enum   
  
# Members

Member| Description  
---|---  
**Advanced**|  The schedule uses a Cron expression.  
**Basic**|  The schedule is a basic run once schedule.  
**Repeating**|  The schedule repeats, for example, every 10 seconds.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Connectors.Schedule.ScheduleType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Connectors.Schedule Namespace](topic6848.md)


