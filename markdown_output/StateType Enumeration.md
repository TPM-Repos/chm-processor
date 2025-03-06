       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateType Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : StateType Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Represents the type of state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum StateType 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [StateType](topic10773.md)  
  
C#|   
---|---  
      
    
    public enum StateType : System.Enum   
  
# Members

Member| Description  
---|---  
**Automatic**|  If a state is an "Automatic" state, it means it is waiting for a DriveWorks Server machine to enact an operation which will move the specification into another state.  
**Paused**|  If a state is a "Paused" state, it means it is waiting for the user to perform an operation which will move the specification into another state.  
**Running**|  If a state is a "Running" state it means it provides forms to the end-user.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Specification.StateType**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Specification Namespace](topic10764.md)


