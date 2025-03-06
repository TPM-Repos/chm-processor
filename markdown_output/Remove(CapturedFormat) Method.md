Remove(CapturedFormat) Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFormatCollection Class](topic14249.md) > [Remove Method](topic14260.md) : Remove(CapturedFormat) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_format_
    The format to remove from the collection.

Glossary Item Box

Removes the given format from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _format_ As [CapturedFormat](topic14240.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFormatCollection](topic14249.md)
    Dim format As [CapturedFormat](topic14240.md)
    Dim value As Boolean
     
    value = instance.Remove(format)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [CapturedFormat](topic14240.md) _format_
    )  
  
#### Parameters

 _format_
    The format to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFormatCollection Class](topic14249.md)   
[CapturedFormatCollection Members](topic14250.md)   
[Overload List](topic14260.md)


