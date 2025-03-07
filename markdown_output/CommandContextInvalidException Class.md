Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandContextInvalidException Class   
[Members](topic672.md)   
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : CommandContextInvalidException Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Thrown when the context passed to a command is not valid for the type of command. 

# Object Model

![](dotnetdiagramimages/image2.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public Class CommandContextInvalidException 
       Inherits System.Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CommandContextInvalidException](topic671.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public class CommandContextInvalidException : System.Exception   
  
# Remarks

A command can be passed context when retrieving its title or image, or when invoking the command. The context is generally specific to the command itself and if the context is not of the wrong type, then the exception is thrown.

# Inheritance Hierarchy

System.Object  
System.Exception  
**DriveWorks.Applications.CommandContextInvalidException**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CommandContextInvalidException Members](topic672.md)   
[DriveWorks.Applications Namespace](topic16.md)


