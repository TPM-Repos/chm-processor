SetDisplayNameCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : SetDisplayNameCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function SetDisplayNameCore( _
       ByVal _name_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim name As String
    Dim value As Boolean
     
    value = instance.SetDisplayNameCore(name)  
  
C#|   
---|---  
      
    
    protected abstract bool SetDisplayNameCore( 
       string _name_
    )  
  
#### Parameters

 _name_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)


