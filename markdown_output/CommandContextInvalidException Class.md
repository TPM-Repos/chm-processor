![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandContextInvalidException Class   
[Members](topic672.md) See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic671.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : CommandContextInvalidException Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Thrown when the context passed to a command is not valid for the type of command. 

# ![](dotnetimages/collapse.gif)Object Model

![](dotnetdiagramimages/image2.png)

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <SerializableAttribute()>
    Public Class CommandContextInvalidException 
       Inherits System.Exception  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CommandContextInvalidException](topic671.md)  
  
C#|   
---|---  
      
    
    [SerializableAttribute()]
    public class CommandContextInvalidException : System.Exception   
  
# ![](dotnetimages/collapse.gif)Remarks

A command can be passed context when retrieving its title or image, or when invoking the command. The context is generally specific to the command itself and if the context is not of the wrong type, then the exception is thrown.

# ![](dotnetimages/collapse.gif)Inheritance Hierarchy

System.Object  
System.Exception  
**DriveWorks.Applications.CommandContextInvalidException**  


# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CommandContextInvalidException Members](topic672.md)   
[DriveWorks.Applications Namespace](topic16.md)

©2024 DriveWorks Ltd. All Rights Reserved.
