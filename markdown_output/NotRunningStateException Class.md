Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotRunningStateException Class   
[Members](topic11059.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : NotRunningStateException Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Thrown when an attempt is made to start a specification based on a project with a specification flow whose initial state is not a running state. 

# Object Model

![](dotnetdiagramimages/image563.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public NotInheritable Class NotRunningStateException 
       Inherits System.Exception  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [NotRunningStateException](topic11058.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public sealed class NotRunningStateException : System.Exception   
  
# Inheritance Hierarchy

System.Object  
System.Exception  
**DriveWorks.Specification.NotRunningStateException**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[NotRunningStateException Members](topic11059.md)   
[DriveWorks.Specification Namespace](topic10764.md)


