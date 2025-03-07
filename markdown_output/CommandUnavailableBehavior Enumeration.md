Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandUnavailableBehavior Enumeration   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : CommandUnavailableBehavior Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Indicates the behavior of UI elements which invoke a command which is not available in the current application state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum CommandUnavailableBehavior 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CommandUnavailableBehavior](topic659.md)  
  
C#|   
---|---  
      
    
    public enum CommandUnavailableBehavior : System.Enum   
  
# Members

Member| Description  
---|---  
**Disable**|  Disables UI elements which invoke the command when it is not available.  
**Hide**|  Hides UI elements which invoke the command when it is not available.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Applications.CommandUnavailableBehavior**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Applications Namespace](topic16.md)


