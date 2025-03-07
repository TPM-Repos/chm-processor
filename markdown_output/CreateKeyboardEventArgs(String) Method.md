Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateKeyboardEventArgs(String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [FormControlValueChangeEventArgs Class](topic2895.md) > [CreateKeyboardEventArgs Method](topic2905.md) : CreateKeyboardEventArgs(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_key_
    The name of the keyboard button that caused this event to occur.

Glossary Item Box

Initializes an instance of [FormControlValueChangeEventArgs](topic2895.md) with values describing a keyboard input. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function CreateKeyboardEventArgs( _
       ByVal _key_ As String _
    ) As [FormControlValueChangeEventArgs](topic2895.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim key As String
    Dim value As [FormControlValueChangeEventArgs](topic2895.md)
     
    value = [FormControlValueChangeEventArgs](topic2895.md).CreateKeyboardEventArgs(key)  
  
C#|   
---|---  
      
    
    public static [FormControlValueChangeEventArgs](topic2895.md) CreateKeyboardEventArgs( 
       string _key_
    )  
  
#### Parameters

 _key_
    The name of the keyboard button that caused this event to occur.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[FormControlValueChangeEventArgs Class](topic2895.md)   
[FormControlValueChangeEventArgs Members](topic2896.md)   
[Overload List](topic2905.md)


