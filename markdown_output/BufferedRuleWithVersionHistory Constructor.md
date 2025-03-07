Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BufferedRuleWithVersionHistory Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [BufferedRuleWithVersionHistory Class](topic6035.md) : BufferedRuleWithVersionHistory Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceRule_
    The rule which will be buffered.

Glossary Item Box

Initializes a new instance of the [BufferedRuleWithVersionHistory](topic6035.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _sourceRule_ As [IHasRule](topic5947.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim sourceRule As [IHasRule](topic5947.md)
     
    Dim instance As New [BufferedRuleWithVersionHistory](topic6035.md)(sourceRule)  
  
C#|   
---|---  
      
    
    public BufferedRuleWithVersionHistory( 
       [IHasRule](topic5947.md) _sourceRule_
    )  
  
#### Parameters

 _sourceRule_
    The rule which will be buffered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[BufferedRuleWithVersionHistory Class](topic6035.md)   
[BufferedRuleWithVersionHistory Members](topic6036.md)


