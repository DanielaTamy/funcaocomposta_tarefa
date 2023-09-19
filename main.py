#FUNÇÃO COMPOSTA - MATEMÁTICA DISCRETA
import sympy as sp

funcao_f = input("Digite a função f(x): ")
funcao_g = input("Digite a função g(x): ")

#tranforma em expressão e x como um simbolo
x = sp.symbols('x')
funcao_f = sp.sympify(funcao_f)
funcao_g = sp.sympify(funcao_g)


#g ° f = g(f(x))
calculo_gf = sp.compose(funcao_g, funcao_f)
print("g(f(x)) =", calculo_gf)

#g ° g = g(f(x))
calculo_gg = sp.compose(funcao_g, funcao_g)
print("g(g(x)) =", calculo_gg)

#f ° f = f(f(x))
calculo_ff = sp.compose(funcao_f, funcao_f)
print("f(f(x)) =", calculo_ff)

#f ° g = f(g(x))
calculo_fg = sp.compose(funcao_f, funcao_g)
print("f(g(x)) =", calculo_fg)

print("se o x = 2:")
valor_x = 2
resultado_gf = calculo_gf.subs(x, valor_x)
print("g(f(2)) =", resultado_gf)

resultado_gg = calculo_gg.subs(x, valor_x)
print("g(g(2)) =", resultado_gg)

resultado_ff = calculo_ff.subs(x, valor_x)
print("f(f(2)) =", resultado_ff)

resultado_fg = calculo_fg.subs(x, valor_x)
print("f(g(2)) =", resultado_fg)
