Tags Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSet Class](topic4106.md) : Tags Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides access to the component tags rule information. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Tags As [ProjectComponentRule](topic6198.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSet](topic4106.md)
    Dim value As [ProjectComponentRule](topic6198.md)
     
    value = instance.Tags  
  
C#|   
---|---  
      
    
    public [ProjectComponentRule](topic6198.md) Tags {get;}  
  
# Remarks

If the component hasn't been loaded by a call to the [LoadComponent](topic4112.md) method, this property will return a null reference (Nothing in Visual Basic).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSet Class](topic4106.md)   
[ProjectComponentSet Members](topic4107.md)


