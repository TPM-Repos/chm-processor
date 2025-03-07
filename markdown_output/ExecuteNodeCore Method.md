Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ExecuteNodeCore Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : ExecuteNodeCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_executeFunc_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub ExecuteNodeCore( _
       ByVal _executeFunc_ As Action _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim executeFunc As Action
     
    instance.ExecuteNodeCore(executeFunc)  
  
C#|   
---|---  
      
    
    protected void ExecuteNodeCore( 
       Action _executeFunc_
    )  
  
#### Parameters

 _executeFunc_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


