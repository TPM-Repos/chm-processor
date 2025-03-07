Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Security Namespace](topic10574.md) > [UserDetails Class](topic10740.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the user identifier. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property Id As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [UserDetails](topic10740.md)
    Dim value As Guid
     
    value = instance.Id  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid Id {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[UserDetails Class](topic10740.md)   
[UserDetails Members](topic10741.md)


