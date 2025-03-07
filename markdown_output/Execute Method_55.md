Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Execute Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification.StandardTasks Namespace](topic11896.md) > [ReleaseDocumentsTask Class](topic12466.md) : Execute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ctx_
    

Glossary Item Box

Overridden to implement the logic required to release one or more documents. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub Execute( _
       ByVal _ctx_ As [SpecificationContext](topic11149.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseDocumentsTask](topic12466.md)
    Dim ctx As [SpecificationContext](topic11149.md)
     
    instance.Execute(ctx)  
  
C#|   
---|---  
      
    
    protected override void Execute( 
       [SpecificationContext](topic11149.md) _ctx_
    )  
  
#### Parameters

 _ctx_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseDocumentsTask Class](topic12466.md)   
[ReleaseDocumentsTask Members](topic12467.md)


