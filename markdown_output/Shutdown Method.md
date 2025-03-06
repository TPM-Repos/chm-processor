Shutdown Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IShutdownable Interface](topic2310.md) : Shutdown Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Shuts down the object. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Shutdown()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IShutdownable](topic2310.md)
     
    instance.Shutdown()  
  
C#|   
---|---  
      
    
    void Shutdown()  
  
# Remarks

This function should act as a way to dispose of an object when processing has finished, rather than performing an immediate disposal.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IShutdownable Interface](topic2310.md)   
[IShutdownable Members](topic2311.md)


