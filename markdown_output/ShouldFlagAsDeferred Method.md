ShouldFlagAsDeferred Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectDrawing Class](topic14516.md) : ShouldFlagAsDeferred Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_deferredComponentNames_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Function ShouldFlagAsDeferred( _
       ByVal _deferredComponentNames_ As IEnumerable(Of String) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDrawing](topic14516.md)
    Dim deferredComponentNames As IEnumerable(Of String)
    Dim value As Boolean
     
    value = instance.ShouldFlagAsDeferred(deferredComponentNames)  
  
C#|   
---|---  
      
    
    protected override bool ShouldFlagAsDeferred( 
       IEnumerable<string> _deferredComponentNames_
    )  
  
#### Parameters

 _deferredComponentNames_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDrawing Class](topic14516.md)   
[ProjectDrawing Members](topic14517.md)


