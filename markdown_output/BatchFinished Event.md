Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
BatchFinished Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [IGenerationService Interface](topic15147.md) : BatchFinished Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a batch of models has been finished. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event BatchFinished As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IGenerationService](topic15147.md)
    Dim handler As EventHandler
     
    AddHandler instance.BatchFinished, handler  
  
C#|   
---|---  
      
    
    event EventHandler BatchFinished  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IGenerationService Interface](topic15147.md)   
[IGenerationService Members](topic15148.md)


