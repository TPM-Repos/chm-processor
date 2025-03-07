Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandContext Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandInvokeEventArgs Class](topic691.md) : CommandContext Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the context passed to the command's [ICommand.Invoke](topic84.md) method. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property CommandContext As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CommandInvokeEventArgs](topic691.md)
    Dim value As Object
     
    value = instance.CommandContext  
  
C#|   
---|---  
      
    
    public object CommandContext {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CommandInvokeEventArgs Class](topic691.md)   
[CommandInvokeEventArgs Members](topic692.md)


