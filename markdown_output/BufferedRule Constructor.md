Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BufferedRule Constructor   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [BufferedRule Class](topic6017.md) : BufferedRule Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceRule_
    The rule which will be buffered.

Glossary Item Box

Initializes a new instance of the [BufferedRule](topic6017.md) type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _sourceRule_ As [IHasRule](topic5947.md) _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim sourceRule As [IHasRule](topic5947.md)
     
    Dim instance As New [BufferedRule](topic6017.md)(sourceRule)  
  
C#|   
---|---  
      
    
    public BufferedRule( 
       [IHasRule](topic5947.md) _sourceRule_
    )  
  
#### Parameters

 _sourceRule_
    The rule which will be buffered.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[BufferedRule Class](topic6017.md)   
[BufferedRule Members](topic6018.md)


