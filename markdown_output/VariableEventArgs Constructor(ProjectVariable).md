VariableEventArgs Constructor(ProjectVariable)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [VariableEventArgs Class](topic5874.md) > [VariableEventArgs Constructor](topic5880.md) : VariableEventArgs Constructor(ProjectVariable)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_variable_
    The variable that was changed.

Glossary Item Box

Initializes a new instance of the [VariableEventArgs](topic5874.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _variable_ As [ProjectVariable](topic4927.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim variable As [ProjectVariable](topic4927.md)
     
    Dim instance As New [VariableEventArgs](topic5874.md)(variable)  
  
C#|   
---|---  
      
    
    public VariableEventArgs( 
       [ProjectVariable](topic4927.md) _variable_
    )  
  
#### Parameters

 _variable_
    The variable that was changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[VariableEventArgs Class](topic5874.md)   
[VariableEventArgs Members](topic5875.md)   
[Overload List](topic5880.md)


