Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EventArguments Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FormControlValueChangeEventArgs Class](topic2895.md) : EventArguments Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all the event arguments associated with the [FormControlValueChangeEventArgs](topic2895.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property EventArguments As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [FormControlValueChangeEventArgs](topic2895.md)
    Dim value As Object
     
    value = instance.EventArguments  
  
C#|   
---|---  
      
    
    public object EventArguments {get;}  
  
#### Property Value

The arguments associated with this event formatted as a DriveWorks table (with headers).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormControlValueChangeEventArgs Class](topic2895.md)   
[FormControlValueChangeEventArgs Members](topic2896.md)


