ShouldGenerate(RuleResults) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [TextDocument Class](topic5643.md) > [ShouldGenerate Method](topic5654.md) : ShouldGenerate(RuleResults) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_results_
    The results of the rules in the document.

Glossary Item Box

Determines whether the document should be generated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overrides Function ShouldGenerate( _
       ByVal _results_ As [RuleResults](topic11136.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TextDocument](topic5643.md)
    Dim results As [RuleResults](topic11136.md)
    Dim value As Boolean
     
    value = instance.ShouldGenerate(results)  
  
C#|   
---|---  
      
    
    public override bool ShouldGenerate( 
       [RuleResults](topic11136.md) _results_
    )  
  
#### Parameters

 _results_
    The results of the rules in the document.

#### Return Value

True if the hasn't been suppressed, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TextDocument Class](topic5643.md)   
[TextDocument Members](topic5644.md)   
[Overload List](topic5654.md)


