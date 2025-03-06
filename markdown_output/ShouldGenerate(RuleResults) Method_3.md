ShouldGenerate(RuleResults) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDocument Class](topic4356.md) > [ShouldGenerate Method](topic4383.md) : ShouldGenerate(RuleResults) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_results_
    The calculated rule results for the document.

Glossary Item Box

Determines whether the document should be generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overridable Function ShouldGenerate( _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDocument](topic4356.md)
    Dim results As [RuleResults](topic11136.md)
    Dim value As Boolean
     
    value = instance.ShouldGenerate(results)  
  
C#|   
---|---  
      
    
    public virtual bool ShouldGenerate( 
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _results_
    The calculated rule results for the document.

#### Return Value

Returns True if the document should be generated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDocument Class](topic4356.md)   
[ProjectDocument Members](topic4357.md)   
[Overload List](topic4383.md)


