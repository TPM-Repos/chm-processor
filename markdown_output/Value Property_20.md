Value Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : Value Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the value of the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Property Value As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim value As Object
     
    instance.Value = value
     
    value = instance.Value  
  
C#|   
---|---  
      
    
    public object Value {get; set;}  
  
# Remarks

This should only be called when [IsDynamic](topic6643.md) is False.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)


